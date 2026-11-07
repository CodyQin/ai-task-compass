/* Local conditional estimates. Capacity is separate from cash benefit. */
(function (root) {
  'use strict';
  function calculate(x) {
    const keys = ['runs','oldMinutes','newMinutes','reviewMinutes','maintenanceHours','upfrontCash','monthlyFees','maintenanceCash','cashSavings','incrementalMargin','avoidedLoss'];
    for (const k of keys) if (typeof x[k] !== 'number' || !Number.isFinite(x[k]) || x[k] < 0) throw new Error('Nonnegative finite numbers required: ' + k);
    if (!Number.isInteger(x.runs)) throw new Error('Monthly runs must be an integer');
    const releasedHours = x.runs * (x.oldMinutes - x.newMinutes - x.reviewMinutes) / 60 - x.maintenanceHours;
    const monthlyCashBenefit = x.cashSavings + x.incrementalMargin + x.avoidedLoss;
    const monthlyIncrementalCashCost = x.monthlyFees + x.maintenanceCash;
    const monthlyNetCash = monthlyCashBenefit - monthlyIncrementalCashCost;
    if (![releasedHours, monthlyCashBenefit, monthlyIncrementalCashCost, monthlyNetCash].every(Number.isFinite)) throw new Error('Inputs exceed supported numeric range');
    const eligible = x.qualityOK === true && x.benefitsConfirmed === true;
    const paybackMonths = eligible && monthlyNetCash > 0 && x.upfrontCash > 0 ? x.upfrontCash / monthlyNetCash : null;
    const firstYearROI = eligible && x.upfrontCash > 0 ? (12 * monthlyNetCash - x.upfrontCash) / x.upfrontCash : null;
    if ([paybackMonths,firstYearROI].some(v=>v!==null && !Number.isFinite(v))) throw new Error('Estimate exceeds supported numeric range');
    return {releasedHours, monthlyCashBenefit, monthlyIncrementalCashCost, monthlyNetCash, eligible,
      paybackMonths, firstYearROI};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {calculate};
  else root.TaskCompassBusiness = {calculate};
})(typeof globalThis !== 'undefined' ? globalThis : this);
